#!/bin/bash
# note taking script from cli

echo $(date): $* >> ~/notes.txt
echo Note saved: $*