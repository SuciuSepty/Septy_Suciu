import customtkinter as ctk
from datetime import date

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Age Calculator (Calculator de Varsta)")
app.geometry("500x500")

# ---------- Functia de calcul ----------

def calculeaza_varsta():
    try:
        zi_n = int(entry_zi_n.get())
        luna_n = int(entry_luna_n.get())
        an_n = int(entry_an_n.get())
        zi_r = int(entry_zi_r.get())
        luna_r = int(entry_luna_r.get())
        an_r = int(entry_an_r.get())

        data_nastere = date(an_n, luna_n, zi_n)
        data_referinta = date(an_r, luna_r, zi_r)

        if data_nastere > data_referinta:
            rezultat_varsta.configure(text="Eroare: Data nasterii este dupa data de referinta.")
            rezultat_viata.configure(text="")
            return

        ani = an_r - an_n
        luni = luna_r - luna_n
        zile = zi_r - zi_n

        if zile < 0:
            luni -= 1
            zile += 30
        if luni < 0:
            ani -= 1
            luni += 12

        rezultat_varsta.configure(text=f"Varsta: {ani} ani, {luni} luni, {zile} zile")

        # Calculul probabilitatii de viata
        if ani < 40:
            sansa = 100
        elif 40 <= ani < 50:
            sansa = 100 - (ani - 40) * 1.5
        elif 50 <= ani < 60:
            sansa = 100 - (ani - 50) * 2
        elif 60 <= ani < 70:
            sansa = 100 - (ani - 60) * 3
        else:
            sansa = 100 - (ani - 70) * 5

        if sansa < 0:
            sansa = 0

        if sansa > 80:
            mesaj = "Probabil in viata"
        elif sansa > 50:
            mesaj = "Sanse moderate"
        elif sansa > 20:
            mesaj = "Putin probabil"
        else:
            mesaj = "Aproape imposibil"

        rezultat_viata.configure(text=f"Posibilitate sa fie in viata: {sansa}% — {mesaj}")

    except:
        rezultat_varsta.configure(text="Introduceti doar numere valide.")
        rezultat_viata.configure(text="")

# ---------- Meniu ----------

label_titlu = ctk.CTkLabel(app, text="DATA NASTERII", font=ctk.CTkFont(size=20, weight="bold"))
label_titlu.pack(pady=10)

frame_dob = ctk.CTkFrame(app)
frame_dob.pack(pady=5)

entry_zi_n = ctk.CTkEntry(frame_dob, placeholder_text="Zi")
entry_luna_n = ctk.CTkEntry(frame_dob, placeholder_text="Luna")
entry_an_n = ctk.CTkEntry(frame_dob, placeholder_text="An")
entry_zi_n.pack(side="left", padx=5)
entry_luna_n.pack(side="left", padx=5)
entry_an_n.pack(side="left", padx=5)

label_ref = ctk.CTkLabel(app, text="DATA ALEASA", font=ctk.CTkFont(size=20, weight="bold"))
label_ref.pack(pady=10)

frame_ref = ctk.CTkFrame(app)
frame_ref.pack(pady=5)

entry_zi_r = ctk.CTkEntry(frame_ref, placeholder_text="Zi")
entry_luna_r = ctk.CTkEntry(frame_ref, placeholder_text="Luna")
entry_an_r = ctk.CTkEntry(frame_ref, placeholder_text="An")
entry_zi_r.pack(side="left", padx=5)
entry_luna_r.pack(side="left", padx=5)
entry_an_r.pack(side="left", padx=5)

btn_calculeaza = ctk.CTkButton(app, text="Calculeaza", command=calculeaza_varsta)
btn_calculeaza.pack(pady=20)

rezultat_varsta = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=16))
rezultat_varsta.pack(pady=5)

rezultat_viata = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=16))
rezultat_viata.pack(pady=5)

app.mainloop()
