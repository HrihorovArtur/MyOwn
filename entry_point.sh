#!/bin/bash

export BROWSER=${BROWSER};
export DOCKER=${DOCKER};

eval "python parallel_runner.py; --clean || true"