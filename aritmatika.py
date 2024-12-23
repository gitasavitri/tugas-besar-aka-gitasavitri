import flet as ft
import sys
import time

sys.setrecursionlimit(100000000)

import time

def aritmatika_iteratif(a, d, n):
    start_time = time.perf_counter()
    total = 0
    for i in range(n):
        total += a + i * d
    end_time = time.perf_counter()
    return total, end_time - start_time

def aritmatika_rekursif(a, d, n):
    if n == 1:
        return a
    else:
        return aritmatika_rekursif(a, d, n - 1) + (a + (n - 1) * d)

def waktu_rekursif(a, d, n):
    start_time = time.perf_counter() 
    result = aritmatika_rekursif(a, d, n)
    end_time = time.perf_counter()
    return result, end_time - start_time


def main(page: ft.Page):
    page.title = "My Arithmetic App"
    page.bgcolor = "#FAEEE0"

    
    header_text = ft.Text(
        value="Penjumlahan Aritmatika",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="#1E2E49",
        font_family="Arial",
        text_align=ft.TextAlign.CENTER
    )

   
    a_input = ft.TextField(
        label="Suku Awal (a)",
        width=300,
        bgcolor="#1E2E49",
        color="white",
        text_align=ft.TextAlign.CENTER
    )
    d_input = ft.TextField(
        label="Selisih (d)",
        width=300,
        bgcolor="#2E3E59",
        color="white",
        text_align=ft.TextAlign.CENTER
    )
    n_input = ft.TextField(
        label="Suku ke- (n)",
        width=300,
        bgcolor="#3E4E69",
        color="white",
        text_align=ft.TextAlign.CENTER
    )

    
    result = ft.Text(value="", size=20, color="#1E2E49", text_align=ft.TextAlign.CENTER)

    
    def calculate(e):
        try:
            a = int(a_input.value)
            d = int(d_input.value)
            n = int(n_input.value)
            method = method_selector.value

            if method == "Iteratif":
                res, duration = aritmatika_iteratif(a, d, n)
            elif method == "Rekursif":
                res, duration = waktu_rekursif(a, d, n)
            else:
                result.value = "Pilih metode perhitungan."
                page.update()
                return

            result.value = (
                f"Hasil penjumlahan dari {n} suku pertama adalah: {res}\n"
                f"Waktu proses: {duration:.6f} detik"
            )
        except ValueError:
            result.value = "Masukkan angka yang valid."
        page.update()

   
    method_selector = ft.Dropdown(
        label="Metode",
        options=[
            ft.dropdown.Option("Iteratif"),
            ft.dropdown.Option("Rekursif")
        ],
        width=300,
        bgcolor="#4E5E79",
        color="white"
    )

   
    calculate_button = ft.ElevatedButton(
        text="Hitung",
        on_click=calculate
    )

   
    content = ft.Column(
        [
            header_text,
            a_input,
            d_input,
            n_input,
            method_selector,
            calculate_button,
            result
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    
    page.add(
        ft.Container(
            content,
            alignment=ft.alignment.center,
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
