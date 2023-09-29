# Hashzap
# botao de iniciar chat
# popup para entrar no chat
# quando entrar no char aparecer para todo mundo
    # A mensagem que voce entrou no chat
    #o campo e o otão de enviar mensagem
# a cada mensagem que enviar 
    #nome: Texto da mensagem

import flet as ft

def main(pagina):
    texto = ft.Text("Hashzao")

    chat = ft.Column()
    nome_usuario = ft.TextField(label="Escreva seu nome")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":    
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            #adicionar menasagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]            
            chat.controls.append(ft.Text(f"{usuario_mensagem}: entou no chat", 
                                size=12,
                                italic=True,
                                color=ft.colors.ORANGE_400))
        pagina.update()


    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto" : campo_mensagem.value, "usuario": nome_usuario.value,
                                "tipo" : "mensagem"})
        #limpar o campo de mensagem
        campo_mensagem.value=""
        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva uma mensagem")
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario" : nome_usuario.value, "tipo" : "entrada"})
        #adicionar o cha
        pagina.add(chat)
        #fechar o popup
        popup.open= False
        # remover o botao iniciar
        pagina.remove(botao_iniciar)
        # criar o campo de mensagem do usuario

        pagina.add(ft.Row(
            [campo_mensagem , botao_enviar_mensagem ]
        ))
        # criar o botao de enviar mensagem do usuario
        pagina.update()


    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title= ft.Text("Ben vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
        )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)
