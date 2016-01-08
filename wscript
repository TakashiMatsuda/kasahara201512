#!/usr/bin/env python

import subprocess

APPNAME = 'SWalign'
VERSION = '1.0.0'

top = '.'
out = 'build'


def configure(ctx):
    ctx.find_program('cp', var='CP')
    ctx.env.PREFIX = ctx.options.prefix
    print(ctx.env.PREFIX)
#    print('-> configuring the project in ' + ctx.path.abspath())


def build(bld):
    bld.install_files('${PREFIX}bin', ['swalign', 'align.py'])
    proc = subprocess.Popen(['chmod', '+x', bld.env.PREFIX+'bin/swalign'],
        stdout=subprocess.PIPE)
    stdout_value = proc.communicate()[0]
    print('\tstdout:', repr(stdout_value))
