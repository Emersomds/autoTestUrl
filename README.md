# autoTestUrl
<h1>Script para teste de url em servido</h1>

<p>O script faz teste se existe uma determinada url em um sistema,
busca na lista de provaveis nome e concatena, faz um for, se a url existi ele retorna Diretorio ou arquivo encontrado, caso não
diretorio ou arquivo não encontrado (404).</p>

<p color="green">Exemplo da execução
http://127.0.0.1:8000/admin.php <br>
[X] Diretório ou arquivo não encontrado (404): admin.php<br>
http://127.0.0.1:8000/login<br>
[+] Deretório ou arquivo encontrado:  login<br>
http://127.0.0.1:8000/sign-up<br>
[X] Diretório ou arquivo não encontrado (404): sign-up<br>
http://127.0.0.1:8000/sign-in<br>
[X] Diretório ou arquivo não encontrado (404): sign-in<br>
http://127.0.0.1:8000/sign_up
[X] Diretório ou arquivo não encontrado (404): sign_up<br>
http://127.0.0.1:8000/sign_in
[X] Diretório ou arquivo não encontrado (404): sign_in<br>
http://127.0.0.1:8000/robots.txt<br>
[+] Deretório ou arquivo encontrado:  robots.txt<br>
http://127.0.0.1:8000/admin<br>
[X] Diretório ou arquivo não encontrado (404): admin<br>
http://127.0.0.1:8000/administrator<br>
[X] Diretório ou arquivo não encontrado (404): administrator<br>
http://127.0.0.1:8000/admin1<br>
[X] Diretório ou arquivo não encontrado (404): admin1<br>
http://127.0.0.1:8000/admin2<br>
[X] Diretório ou arquivo não encontrado (404): admin2<br>
http://127.0.0.1:8000/backup<br>
[X] Diretório ou arquivo não encontrado (404): backup<br>
http://127.0.0.1:8000/bkp<br>
[X] Diretório ou arquivo não encontrado (404): bkp<br>
http://127.0.0.1:8000/bkp.zip<br>
[X] Diretório ou arquivo não encontrado (404): bkp.zip<br>
http://127.0.0.1:8000/index.php<br>
[+] Deretório ou arquivo encontrado:  index.php<br>
http://127.0.0.1:8000/vendor<br>
[X] Diretório ou arquivo não encontrado (404): vendor</p>

<h2>Lista de nome </h2>
admin.php<br>
login<br>
sign-up<br>
sign-in<br>
sign_up<br>
sign_in<br>
robots.txt<br>
admin<br>
administrator<br>
admin1<br>
admin2<br>
backup<br>
bkp<br>
bkp.zip<br>
index.php<br>
vendor<br>



