#!/usr/bin/env python
"""
open vscode and create debug configuration for bazel target in sandbox
"""
import sys
import os
from mako.template import Template
from mako.lookup import TemplateLookup

launch_file_tempate = """\
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "debug ${target}",
      "type": "cppdbg",
      "request": "launch",
      "program": "${"${workspaceFolder}"}/${binPath}/${target}",
      "args": [],
      "stopAtEntry": true,
      "cwd": "${"${workspaceFolder}"}",
      "environment": [],
      "externalConsole": false,
      "MIMode": "lldb",
      "internalConsoleOptions": "openOnSessionStart"
    }
  ]
}
"""

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("usage: python {0} taget_name".format(os.path.basename(__file__)))
        exit(-1)

    print("compile debug binary for " + sys.argv[1])
    os.system("bazel build " + " ".join(sys.argv[1:]) + " --compilation_mode=dbg")

    print("setup debug workspace for " + sys.argv[1])

    workspace_name = os.path.basename(os.path.realpath("."))
    sandbox_path = os.path.realpath("bazel-" + workspace_name)
    print("sandbox path: " + sandbox_path)

    bin_path = os.path.realpath("bazel-bin")
    bin_rel_path = os.path.relpath(bin_path, sandbox_path)

    os.chdir(sandbox_path)
    if not os.path.isdir(".vscode"):
        os.mkdir(".vscode")

    launch_file = ".vscode/launch.json"
    with open(launch_file, "w") as f:
        template = Template(launch_file_tempate)
        f.write(template.render(target=sys.argv[1], binPath=bin_rel_path))

    os.system("code " + sandbox_path)
