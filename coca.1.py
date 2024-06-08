import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pyperclip
import webbrowser
import os

def copy_to_clipboard(text):
    pyperclip.copy(text)

def open_email(email):
    webbrowser.open(f"mailto:{email}")

def show_home():
    for widget in content_frame.winfo_children():
        widget.destroy()

    title = tk.Label(content_frame, text=" Stolarija ĆOĆA MONT", font=("Helvetica", 26, "bold"), bg="#f5f5f5")
    title.pack(pady=(20, 10))

    # Postavljanje slike na početnu stranicu
    logo_path = "C:/Users/David/Downloads/LOGO_2-removebg-preview (1).png"
    if os.path.exists(logo_path):
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((200, 200), Image.Resampling.LANCZOS)  # Ispravljeno ovde
        logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = tk.Label(content_frame, image=logo_photo)
        logo_label.image = logo_photo  # Čuvanje reference na sliku
        logo_label.pack(pady=(20, 10))
    else:
        error_label = tk.Label(content_frame, text="Slika nije pronađena.", font=("Helvetica", 14), bg="#f5f5f5")
        error_label.pack(pady=20)

    # Opis
    description = tk.Label(
        content_frame,
        text=(
            "U ponudi širok asortiman PVC i aluminijumske stolarije vrhunskog kvaliteta:\n\n"
        
            
            "- Prozore i vrata\n"
            "- Balkonska vrata\n"
            "- Klizna vrata\n"
            "- Rolo i segmentna vrata\n"
            "- Pivot vrata\n"
            "- Tuš kabine\n"
            "- Staklene fasade\n"
            "- Staklene ograde\n"
            "- Roletne\n"
            "- Komarnike\n"
            "- Uskočno glizne i klizne elemente\n"
            "- I još mnogo toga!\n"
        ),
        font=("Helvetica", 14),
        justify="left",
        bg="#f5f5f5"
    )
    description.pack(pady=10, padx=10, anchor="w")

def show_about():
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Okvir za sadržaj sa slikom i tekstom
    about_frame = tk.Frame(content_frame, bg="#f5f5f5")
    about_frame.pack(fill="both", expand=True)

    # Okvir za sliku
    image_frame = tk.Frame(about_frame, bg="#f5f5f5")
    image_frame.pack(side="left", fill="y")

    # Učitavanje slike za pozadinu
    bg_image_path = "C:/Users/David/Desktop/slika.vukasin.jpg"  # Putanja do slike slika.vukasin.jpg
    if os.path.exists(bg_image_path):
        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((400, 600), Image.Resampling.LANCZOS)  # Ispravljeno ovde
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(image_frame, image=bg_photo)
        bg_label.image = bg_photo  # Čuvanje reference na sliku
        bg_label.pack()
    else:
        error_label = tk.Label(image_frame, text="Pozadinska slika nije pronađena.", font=("Helvetica", 14), bg="#f5f5f5")
        error_label.pack(pady=20)

    # Okvir za tekst
    text_frame = tk.Frame(about_frame, bg="#f5f5f5")
    text_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

    about_label = tk.Label(
        text_frame,
        text=(
            "Dobrodošli na veb-sajt ĆOĆA MONT\n"
            "gde je kvalitet za vaš dom glavna misija.\n"
            "Ja sam Vukašin, osnivač i vlasnik ove kompanije.\n"
            "Specijalizujem se za ugradnju, popravku, montažu i\n"
            "demontažu PVC i aluminijumske stolarije. Sa svojim iskustvom\n"
            "i posvećenošću detaljima, pružam vrhunske usluge koje\n"
            "odgovaraju svim vašim potrebama za stolarijom. Bez obzira\n"
            "na veličinu projekta, moj cilj je da vam pružim najkvalitetnija\n"
            "rešenja koja će unaprediti estetiku i funkcionalnost vašeg doma.\n"
            "Verujem u transparentnost, pouzdanost i stručnost u svakom aspektu\n"
            "svog rada. Svaki projekat tretiram kao da radim za svoj dom,\n"
            "osiguravajući da svaki detalj bude savršen.\n"
        ),
        font=("Helvetica", 14),
        justify="left",
        bg="#f5f5f5"
    )
    about_label.pack(fill="both", expand=True)

    more_options_button = tk.Button(text_frame, text="Još opcija", font=("Helvetica", 12, "bold"), bg="#c0c0c0", command=show_more_options)
    more_options_button.pack(pady=20)

def show_more_options():
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Kontakt telefon
    contact_phone_frame = tk.Frame(content_frame, bg="#f5f5f5")
    contact_phone_frame.pack(pady=5, anchor="w", padx=10)

    contact_phone_label = tk.Label(contact_phone_frame, text="Kontakt telefon: 0628658333", font=("Helvetica", 12, "bold"), bg="#f5f5f5")
    contact_phone_label.pack(side="left")

    copy_phone_button = tk.Button(contact_phone_frame, text="Kopiraj", command=lambda: copy_to_clipboard("0628658333"), bg="#d0d0d0")
    copy_phone_button.pack(side="left", padx=10)

    # Kontakt email
    contact_email_frame = tk.Frame(content_frame, bg="#f5f5f5")
    contact_email_frame.pack(pady=5, anchor="w", padx=10)

    contact_email_label = tk.Label(contact_email_frame, text="Kontakt putem email-a: banovicvukasin8@gmail.com", font=("Helvetica", 12, "bold"), bg="#f5f5f5", fg="blue", cursor="hand2")
    contact_email_label.pack(side="left")
    contact_email_label.bind("<Button-1>", lambda e: open_email("banovicvukasin8@gmail.com"))

    copy_email_button = tk.Button(contact_email_frame, text="Kopiraj", command=lambda: copy_to_clipboard("banovicvukasin8@gmail.com"), bg="#d0d0d0")
    copy_email_button.pack(side="left", padx=10)

def show_gallery():
    for widget in content_frame.winfo_children():
        widget.destroy()

    title = tk.Label(content_frame, text="Galerija", font=("Helvetica", 26, "bold"), bg="#f5f5f5")
    title.pack(pady=(20, 10))

    gallery_frame = tk.Frame(content_frame, bg="#f5f5f5")
    gallery_frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Ovdje dodajte slike u galeriju
    image_paths = [
        "C:/Users/David/Desktop/vukasin.vrata.jpg",
        "C:/Users/David/Desktop/vukasin.vrata.prozor.jpg",
        "C:/Users/David/Desktop/vukasin.slika2.jpg",
        "C:/Users/David/Desktop/vukasin.slika3.jpg"
    ]

    for image_path in image_paths:
        if os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.Resampling.LANCZOS)  # Ispravljeno ovde
            photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(gallery_frame, image=photo, bg="#f5f5f5")
            image_label.image = photo  # Čuvanje reference na sliku
            image_label.pack(side="left", padx=10, pady=10)
        else:
            error_label = tk.Label(gallery_frame, text=f"Slika nije pronađena: {image_path}", font=("Helvetica", 14), bg="#f5f5f5")
            error_label.pack(pady=20)

def main():
    global content_frame

    # Inicijalizacija glavnog prozora
    root = tk.Tk()
    root.title("PVC Stolarija ĆOĆA MONT")
    root.geometry("800x600")
    root.configure(bg="#e0e0e0")  # Boja pozadine prozora

    # Gornji meni
    menu_frame = tk.Frame(root, bg="#e0e0e0")
    menu_frame.pack(side="top", anchor="ne", pady=10, padx=20)

    home_button = tk.Button(menu_frame, text="Home", font=("Helvetica", 12, "bold"), bg="#c0c0c0", command=show_home)
    home_button.pack(side="left", padx=10)

    about_button = tk.Button(menu_frame, text="About", font=("Helvetica", 12, "bold"), bg="#c0c0c0", command=show_about)
    about_button.pack(side="left", padx=10)

    gallery_button = tk.Button(menu_frame, text="Galerija", font=("Helvetica", 12, "bold"), bg="#c0c0c0", command=show_gallery)
    gallery_button.pack(side="left", padx=10)

    # Okvir za sadržaj
    content_frame = tk.Frame(root, bg="#f5f5f5", bd=2, relief="solid")
    content_frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Prikazivanje početne stranice
    show_home()

    # Footer
    footer = tk.Label(root, text="Hvala što ste posetili naš sajt!", font=("Helvetica", 10, "italic"), bg="#e0e0e0")
    footer.pack(side="bottom", pady=10)

    # Pokretanje glavne petlje
    root.mainloop()

if __name__ == "__main__":
    main()
