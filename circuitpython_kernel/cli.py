# # -*- coding: utf-8 -*-
#
# import click
#
# import json
# import os
# import sys
#
# from ipykernel.kernelapp import IPKernelApp
# from .circuitpython_kernel import CircuitPyKernel
# from jupyter_client.kernelspec import install_kernel_spec
# from IPython.utils.tempdir import TemporaryDirectory
#
# kernel_json = {"argv": [sys.executable, "-m", "circuitpython_kernel", "-f", "{connection_file}"],
#  "display_name":"CircuitPython",
#  "language":"python",
# }
#
# def install_my_kernel_spec(user=True):
#     with TemporaryDirectory() as td:
#         os.chmod(td, 0o755) # Starts off as 700, not user readable
#         with open(os.path.join(td, 'kernel.json'), 'w') as f:
#             json.dump(kernel_json, f, sort_keys=True)
#         # TODO: Copy resources once they're specified
#
#         print('Installing CircuitPython kernel spec')
#         install_kernel_spec(td, 'CircuitPyKernel', user=user, replace=True)
#
# def _is_root():
#     try:
#         return os.geteuid() == 0
#     except AttributeError:
#         return False # assume not an admin on non-Unix platforms
#
# # def main(argv=[]):
#     # user = '--user' in argv or not _is_root()
#     # install_my_kernel_spec(user=user)
#
# @click.command()
# def main(argv=[]):
#     """Console script for circuitpython_kernel"""
#     click.echo("Replace this message by putting your code into "
#                "circuitpython_kernel.cli.main")
#     click.echo("See click documentation at http://click.pocoo.org/")
#
# @click.command('install')
# def install():
#     click.echo("Installing")
#     user = '--user' in argv or not _is_root()
#     install_my_kernel_spec(user=user)
#
#     IPKernelApp.launch_instance(kernel_class=CircuitPyKernel)
#
# if __name__ == "__main__":
#     main()
