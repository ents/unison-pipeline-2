#!/usr/bin/env nextflow

nextflow.enable.dsl=2

params.data_file = 'data.yaml'
params.out_dir = 'results'

process runPythonExample {
    publishDir '.', mode: 'copy'
    tag 'Run python-example container'

    container 'python:3.11'

    input:
    path data_file

    output:
    path 'result.txt', emit: result

    script:
    """
    mkdir -p /data
    cp ${data_file} /data/data.yaml
    python3 /app/query.py
    cp /data/result.txt result.txt
    """
}

workflow {
    runPythonExample(file(params.data_file))
}