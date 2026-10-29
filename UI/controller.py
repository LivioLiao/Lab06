import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def mostra_strumenti(self, e):  #Gestisce il click su Mostra

        strumenti = self._model.get_strumenti()
        self._view.lista_strumenti.controls.clear()

        if strumenti is None:
            self._view.show_alert("Errore durante il caricamento degli strumenti dal database.")
        elif len(strumenti) == 0:
            self._view.lista_strumenti.controls.append(ft.Text("Nessuno strumento presente nel deposito."))
        else:
            for s in strumenti:
                stato = "✅" if s.disponibile else "⛔"
                self._view.lista_strumenti.controls.append(ft.Text(f"{stato} {s}"))

        self._view.update()

    def cerca_strumenti(self, e):    #Gestisce il click su cerca

        tipo = self._view.input_tipo_strumento.value.strip()

        self._view.lista_strumenti_ricerca.controls.clear()

        if not tipo:
            self._view.show_alert("Inserisci un tipo di strumento da cercare.")
            self._view.update()
            return

        strumenti = self._model.cerca_strumenti_per_tipo(tipo)

        if strumenti is None:
            self._view.show_alert("Errore durante la ricerca nel database.")
        elif len(strumenti) == 0:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text(f"Nessun {tipo} trovato."))
        else:
            for s in strumenti:
                stato = "✅" if s.disponibile else "⛔"
                self._view.lista_strumenti_ricerca.controls.append(ft.Text(f"{stato} {s}"))

        self._view.update()