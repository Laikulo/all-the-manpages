#!/bin/ysh

apk list | split($_)[0]
