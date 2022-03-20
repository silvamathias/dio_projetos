# Tutorial GitHub

## Criando chave ssh

### sistema linux :penguin: 

1. escreva o código abaixo no terminal e depois informe uma senha e confirme ou precione **enter** para não atribuir senha;

'ssh-keygen -t ed25519 -C seu_email_aqui@provedor_email.com'

2. procure a linha abaixo onde informará o local que as chaves foram salvas;

'Enter file in which to save the key (/home/seu usuário/.ssh/id_ed25519):' 

3. Navegue até a pasta informada;

'cd /home/seu usuário/.ssh/'

4. Use o **cat** seguido do nome do arquivo com o final **.pub** (chave pública) para visualisá-la;
'cat id_ed25519.pub' 

5. NO **Github** faça.

	- **clique** na sua **foto**;
	-  selecione **Settings**;
	-  Procure por **SSH ang GPG Keys** e clique;
	-  Precione o botão **New SSH Key**;
	- Escolha um nome para a chave e coloque no campo **Title**;
	- Cole a chave do item **4** no campo **Key**;
	- Clique em **Add SSH Key**.

6.  Retorne ao terminal e digite;

'eval $(ssh-agent -s)'

7. Escreva o código abaixo e precione **Enter**
'ssh-add id_ed25519'


