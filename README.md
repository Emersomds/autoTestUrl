# autoTestUrl
Script para teste de url em servido

O script faz teste se existe uma determinada url em um sistema,
busca na lista de provaveis nome e concatena, faz um for, se a url existi ele retorna Diretorio ou arquivo encontrado, caso não
diretorio ou arquivo não encontrado (404).

Exemplo da execução
http://127.0.0.1:8000/admin.php
[X] Diretório ou arquivo não encontrado (404): admin.php
http://127.0.0.1:8000/login
[+] Deretório ou arquivo encontrado:  login
http://127.0.0.1:8000/sign-up
[X] Diretório ou arquivo não encontrado (404): sign-up
http://127.0.0.1:8000/sign-in
[X] Diretório ou arquivo não encontrado (404): sign-in
http://127.0.0.1:8000/sign_up
[X] Diretório ou arquivo não encontrado (404): sign_up
http://127.0.0.1:8000/sign_in
[X] Diretório ou arquivo não encontrado (404): sign_in
http://127.0.0.1:8000/robots.txt
[+] Deretório ou arquivo encontrado:  robots.txt
http://127.0.0.1:8000/admin
[X] Diretório ou arquivo não encontrado (404): admin
http://127.0.0.1:8000/administrator
[X] Diretório ou arquivo não encontrado (404): administrator
http://127.0.0.1:8000/admin1
[X] Diretório ou arquivo não encontrado (404): admin1
http://127.0.0.1:8000/admin2
[X] Diretório ou arquivo não encontrado (404): admin2
http://127.0.0.1:8000/backup
[X] Diretório ou arquivo não encontrado (404): backup
http://127.0.0.1:8000/bkp
[X] Diretório ou arquivo não encontrado (404): bkp
http://127.0.0.1:8000/bkp.zip
[X] Diretório ou arquivo não encontrado (404): bkp.zip
http://127.0.0.1:8000/index.php
[+] Deretório ou arquivo encontrado:  index.php
http://127.0.0.1:8000/vendor
[X] Diretório ou arquivo não encontrado (404): vendor

Lista de nome 
admin.php
login
sign-up
sign-in
sign_up
sign_in
robots.txt
admin
administrator
admin1
admin2
backup
bkp
bkp.zip
index.php
vendor



