#!/usr/bin/env bash

function generate {
  file_base=$1
  output_dir=/tmp/wapps/${file_base}
  rm -r ${output_dir}
  mkdir -p ${output_dir}
  if test  ${file_base}.rst -nt ${file_base}.tex
  then
    rst2latex-tweaked.py ${file_base}.rst > ${file_base}.tex
    pdflatex -output-directory ${output_dir} ${file_base}.tex
    pdflatex -output-directory ${output_dir} ${file_base}.tex
    pdflatex -output-directory ${output_dir} ${file_base}.tex # Regeneate latex so references are OK
    cp ${output_dir}/${file_base}.pdf downloads/pdfs
  fi
};

cd content

mkdir -p downloads/pdfs
generate wyk1
generate wyk2