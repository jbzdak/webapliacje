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

function generate_ipynb {
  file_base=$1
  output_dir="/tmp/wapps/${file_base}"
  rm -r "${output_dir}"
  mkdir -p "${output_dir}"
  # echo test ${file_base}.ipynb -nt ${file_base}.tex
  if test  ${file_base}.ipynb -nt ${file_base}.tex
  then
#    rst2latex-tweaked.py ${file_base}.rst > ${file_base}.tex
    ipython nbconvert --to html ${file_base}.ipynb
    ipython nbconvert --to latex ${file_base}.ipynb
    sed '-i.back' 's/\\documentclass{article}/\\documentclass{article}\\usepackage[T1]{fontenc}/' "${file_base}.tex"
    sed -i 's/\\usepackage{booktabs}/\\usepackage{booktabs}\\usepackage{upquote}/' "${file_base}.tex"
    sed -i 's/\\usepackage{booktabs}/\\usepackage{booktabs}\\usepackage{textcomp}/' "${file_base}.tex"
    pdflatex -output-directory ${output_dir} ${file_base}.tex
    pdflatex -output-directory ${output_dir} ${file_base}.tex
    pdflatex -output-directory ${output_dir} ${file_base}.tex # Regeneate latex so references are OK
    cp "${output_dir}/${file_base}.pdf" "${ROOT}/content/downloads/pdfs"
  fi
};


source source.me

ROOT=$(pwd)

cd content

mkdir -p downloads/pdfs

generate wyk1
generate wyk2
generate wyk4
generate wyk5
generate wyk6

generate zaj2
generate zaj3
generate zaj4
# {#generate zaj5##}

cd ${ROOT}
cd content/static/zaj3

generate_ipynb zaj1-blok1
generate_ipynb zaj1-blok2
generate_ipynb zaj1-blok3
generate_ipynb zaj1-blok4
generate_ipynb zaj3-blok4