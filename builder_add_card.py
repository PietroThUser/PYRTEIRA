from flet import *


name_card = TextField(label="Nome do cartão (Invente um nome para esse cartão)",
                      label_style=TextStyle(
                          size=13
                      ),
                      border_color=colors.BACKGROUND
                      )

ncard = TextField(label="Número do cartão",
                  label_style=TextStyle(
                      size=13
                  ),
                  border_color=colors.BACKGROUND
                  )

vcard = TextField(label="Validade do catão",
                  label_style=TextStyle(
                      size=13
                  ),
                  border_color=colors.BACKGROUND
                  )

name_client = TextField(label="De quem é esse cartão (Nome completo)",
                        label_style=TextStyle(
                            size=13
                        ),
                        border_color=colors.BACKGROUND
                        )

bank_card = TextField(label="Banco (De qual banco é esse cartão)",
                      label_style=TextStyle(
                          size=13
                      ),
                      border_color=colors.BACKGROUND
                      )

cvc_card = TextField(label="CVC",
                     label_style=TextStyle(
                         size=13
                     ),
                     border_color=colors.BACKGROUND
                     )


class BuilderAddCard:
    containerContent = Column([
        Text(""),
        name_card,
        ncard,
        vcard,
        name_client,
        cvc_card,
        bank_card
    ])

    homeButton = ElevatedButton("Voltar a página inicial", 
        color=colors.WHITE, 
        bgcolor=colors.RED,
        height=50,
        width=10000,
        expand=True)
    
    confirmButton = ElevatedButton("Confirmar",
        color=colors.WHITE,
        bgcolor=colors.GREEN,
        height=50,
        width=10000,
        expand=True)


    app: SafeArea = SafeArea(
        Column([
            Text("Configure seu cartão",
                weight=FontWeight.W_700,
                size=25),

            Container(
                content=containerContent        
            ),

            Column([
                Row([
                    homeButton
                ]),
                Row([
                    confirmButton
                ])
            ],
            alignment=MainAxisAlignment.END
            )
        ],
        expand=True
        ),
        expand=True
    )