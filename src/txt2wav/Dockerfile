FROM ubuntu

RUN apt update -y && apt install -y espeak-ng

ENV input=file.txt

ENV output=file.wav

ENV voice=en-us

CMD espeak-ng -v "${voice}" -f "${input}" -w "${output}"
