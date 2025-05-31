def iniciar_assistente():
        print("Olá! Eu sou seu assistente virtual de PNL.")
            print("Como posso ajudar você hoje?")
                while True:
                        entrada = input("Você: ").strip().lower()
                                
                                        if entrada in ["sair", "tchau", "encerrar"]:
                                                    print("Assistente: Até logo! Cuide da sua mente!")
                                                                break
                                                                        elif "ansiedade" in entrada:
                                                                                    print("Assistente: Que tal uma respiração profunda? Inspire... expire... Você está no controle.")
                                                                                            elif "desânimo" in entrada or "motivação" in entrada:
                                                                                                        print("Assistente: Lembre-se: cada passo, por menor que seja, te aproxima do seu objetivo.")
                                                                                                                elif "medo" in entrada:
                                                                                                                            print("Assistente: O medo é um sinal de que você está crescendo. Encare com coragem!")
                                                                                                                                    else:
                                                                                                                                                print("Assistente: Interessante! Conte-me mais sobre isso.")

                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                    iniciar_assistente()