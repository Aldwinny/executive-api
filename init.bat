@ECHO off
if not exist ".\bin" mkdir .\bin
py -X pycache_prefix=bin -m lib.main hello world