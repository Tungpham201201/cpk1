#!/usr/bin/python

# Copyright (C) Anasov <me@anasov.ly> - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Anasov <me@anasov.ly>, 05, May, 2024.

import random
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
from cpkrst import CPMEwan

__CHANNEL_USERNAME__ = "Roasted2001"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name =  "        ░█████╗░░░░██████╗░░░░██╗░░██╗░░░░░███╗░░\n"
    brand_name += "        ██╔══██╗░░░██╔══██╗░░░██║░██╔╝░░░░████║░░\n"
    brand_name += "        ██║░░╚═╝░░░██████╔╝░░░█████═╝░░░░██╔██║░░\n"
    brand_name += "        ██║░░██╗░░░██╔═══╝░░░░██╔═██╗░░░░╚═╝██║░░\n"
    brand_name += "        ╚█████╔╝░░░██║░░░░░░░░██║░╚██╗░░░███████╗\n"
    brand_name += "        ░╚════╝░░░░╚═╝░░░░░░░░╚═╝░░╚═╝░░░╚══════╝\n"
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    console.print("[bold yellow]      ♕ CPKVN[/bold yellow][bold red]: Car Parking 1 Hacking Tool VietNames.[/bold red]")
    console.print("[bold yellow]   ==================================================[/bold yellow]")
    console.print("[bold red]    《 Lưu ý:[/bold red][bold red]: Đăng xuất tài khoản trước khi hack 》", end="\n\n")

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
            console.print("[bold yellow]   ========[ CHI TIẾT TÀI KHOẢN ]========[/bold yellow]")
            console.print(f"[bold yellow]   Name   :[/bold yellow][bold green] { (data.get('Name') if 'Name' in data else 'UNDEFINED') }.[/bold green]")
            console.print(f"[bold yellow]   LocalID:[/bold yellow][bold green] { (data.get('localID') if 'localID' in data else 'UNDEFINED') }.[/bold green]")
            console.print(f"[bold yellow]   Money  :[/bold yellow][bold green] { (data.get('money') if 'money' in data else 'UNDEFINED') }.[/bold green]")
            console.print(f"[bold yellow]   Coins  :[/bold yellow][bold green] { (data.get('coin') if 'coin' in data else 'UNDEFINED') }.[/bold green]", end="\n\n")
        else:
            console.print("[bold red]! ERROR: Tài Khoản Chưa Được Tạo Không thể Đăng Nhập !.[/bold red]")
            exit(1)
    else:
        console.print("[bold red]! ERROR: Sai Tài Khoản Hoặc Mật Khẩu !.[/bold red]")
        exit(1)

def load_key_data(cpm):
    data = cpm.get_key_data()
    console.print("[bold yellow]========《 Tất Cả Các Hack 》========[/bold yellow]")
    console.print(f"[bold green]Credits:[/bold green] [bold yellow]{ (data.get('coins') if not data.get('is_unlimited') else 'ROASTED_AMONYMOUS') }[/bold yellow].", end="\n\n")

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            console.print(f"[bold red]   ⚠ {tag} Không thể để trống, hãy thử lại ⚠[/bold red]")
        else:
            return value

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold yellow]   Email tài khoản   : [/bold yellow]", "Email", password=False)
        acc_password = prompt_valid_value("[bold yellow]   Mật khẩu tài khoản: [/bold yellow]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold yellow]   Key đăng nhập     :[/bold yellow]", "Access Key", password=False)
        console.print("[bold #00dcff]   [%] Đang đăng nhập tài khoản[/bold #00dcff]: ", end=None)
        cpm = CPMEwan(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                console.print("[bold red]Không tìm thấy tài khoản[/bold red].")
                sleep(2)
                continue
            elif login_response == 101:
                console.print("[bold red]Sai Mật Khẩu[/bold red].")
                sleep(2)
                continue
            elif login_response == 103:
                console.print("[bold red]Key không hợp lệ[/bold red].")
                sleep(2)
                continue
            else:
                console.print("[bold red]Hãy thử lại[/bold red].")
                console.print("[bold yellow]⚠ Note: Hãy chắc chắn rằng bạn đã điền đầy đủ ⚠[/bold yellow]")
                sleep(2)
                continue
        else:
            console.print("[bold green]Đã thành công[/bold green].")
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
            console.print("[bold yellow](01):[/bold yellow][bold green] Tiền tùy chỉnh.[/bold green]")
            console.print("[bold yellow](02):[/bold yellow][bold green] Xu tùy chỉnh.[/bold green]")
            console.print("[bold yellow](03):[/bold yellow][bold green] King Rank.[/bold green]")
            console.print("[bold yellow](04):[/bold yellow][bold green] Thay đổi ID.[/bold green]")
            console.print("[bold yellow](05):[/bold yellow][bold green] Thay đổi tên 1.[/bold green]")
            console.print("[bold yellow](06):[/bold yellow][bold green] Thay đổi tên 2 (Màu).[/bold green]")
            console.print("[bold yellow](07):[/bold yellow][bold green] Biển số xe.[/bold green]")
            console.print("[bold yellow](08):[/bold yellow][bold green] Xóa tài khoản.[/bold green]")
            console.print("[bold yellow](09):[/bold yellow][bold green] Đăng kí tài khoản.[/bold green]")
            console.print("[bold yellow](10):[/bold yellow][bold green] Xóa bạn bè.[/bold green]")
            console.print("[bold yellow](11):[/bold yellow][bold green] Mở khóa tất cả xe trả phí.[/bold green]")
            console.print("[bold yellow](12):[/bold yellow][bold green] Mở khóa tất cả các xe.[/bold green]")
            console.print("[bold yellow](13):[/bold yellow][bold green] Mở khóa tất cả còi báo động.[/bold green]")
            console.print("[bold yellow](14):[/bold yellow][bold green] Mở khóa động cơ w16.[/bold green]")
            console.print("[bold yellow](15):[/bold yellow][bold green] Mở khóa tất cả còi xe[/bold green]")
            console.print("[bold yellow](16):[/bold yellow][bold green] Mở khóa không hỏng động cơ.[/bold green]")
            console.print("[bold yellow](17):[/bold yellow][bold green] Mở khóa không giới hạn xăng.[/bold green]")
            console.print("[bold yellow](18):[/bold yellow][bold green] Mở khóa nhà 3.[/bold green]")
            console.print("[bold yellow](19):[/bold yellow][bold green] Mở khóa khói[/bold green]")
            console.print("[bold yellow](20):[/bold yellow][bold green] Chỉnh sửa đua thắng.[/bold green]")
            console.print("[bold yellow](21):[/bold yellow][bold green] Chỉnh sửa đua thua.[/bold green]")
            console.print("[bold yellow](22):[/bold yellow][bold green] Sao chép tài khoản.[/bold green]")
            console.print("[bold yellow](0) :[/bold yellow][bold yellow] Đăng xuất tài khoản.[/bold yellow]", end="\n\n")
            service = IntPrompt.ask(f"[bold #00dcff] 🛠 Chọn một dịch vụ [/bold #00dcff][bold red][1 => {choices[-1]} hoặc 0][/bold red]", choices=choices, show_choices=False)
            if service == 0: # Exit
                console.print(f"[bold #00dcff]Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
            elif service == 1: # Increase Money
                console.print("[bold yellow]⚠ Nhập số tiền bạn muốn ⚠.[/bold yellow]")
                amount = IntPrompt.ask("[bold yellow]Số lượng.[/bold yellow]")
                console.print("[bold #00dcff][%] Đang lưu dữ liệu[/bold #00dcff]: ", end=None)
                if amount > 0 and amount <= 50000000:
                    if cpm.set_player_money(amount):
                        console.print("[bold green]Đã thành công.[/bold green]")
                        console.print("[bold green]==================================[/bold green]")
                        answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không?[/bold yellow]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                        else: continue
                    else:
                        console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                        console.print("[bold yellow]⚠ Vui lòng thử lại ⚠.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Vui lòng sử dụng giá trị hợp lệ ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                console.print("[bold yellow][!] Nhập số xu bạn muốn.[/bold yellow]")
                amount = IntPrompt.ask("[bold yellow] Số lượng[/bold yellow]")
                console.print("[bold #00dcff][%] Đang lưu dữ liệu[/bold #00dcff]: ", end=None)
                if amount > 0 and amount <= 500000:
                    if cpm.set_player_coins(amount):
                        console.print("[bold green]Đã thành công[/bold green]")
                        console.print("[bold green]==================================[/bold green]")
                        answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold blue][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold blue][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                        else: continue
                    else:
                        console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                        console.print("[bold yellow]⚠ Vui lòng thử lại ⚠[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Vui lòng sử dụng giá trị hợp lệ ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold yellow]⚠ Ghi chú: nếu rank king không xuất hiện trong trò chơi, hãy đóng nó lại và mở lại vài lần.[/bold yellow]", end=None)
                console.print("[bold yellow]⚠ Ghi chú: Không thể làm rank King trên cùng một tài khoản hai lần. [/bold yellow]", end=None)
                sleep(2)
                console.print("[bold #00dcff][%] Đang tạo rank king[/bold #00dcff]: ", end=None)
                if cpm.set_player_rank():
                    console.print("[bold green]Đã thành công.[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold blue][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold blue][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                    else: continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                console.print("[bold yellow][!] Nhập ID mới của bạn.[/bold yellow]")
                new_id = Prompt.ask("[bold yellow][?] ID[/bold yellow]")
                console.print("[bold #00dcff][%] Đang lưu dữ liệu[/bold #00dcff]: ", end=None)
                if len(new_id) >= 4 and len(new_id) <= 1000 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        console.print("[bold green]Đã thành công.[/bold green]")
                        console.print("[bold green]==================================[/bold green]")
                        answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold blue][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold blue][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                        else: continue
                    else:
                        console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                        console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Vui lòng sử dụng ID khác ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                console.print("[bold yellow][!] Nhập tên mới của bạn.[/bold yellow]")
                new_name = Prompt.ask("[bold yellow][?] Tên[/bold yellow]")
                console.print("[bold #00dcff][%] Đang lưu dữ liệu[/bold #00dcff]: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 30:
                    if cpm.set_player_name(new_name):
                        console.print("[bold green]Đã thành công.[/bold green]")
                        console.print("[bold green]==================================[/bold green]")
                        answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold blue][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold blue][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                        else: continue
                    else:
                        console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                        console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Vui lòng sử dụng giá trị hợp lệ ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                console.print("[bold yellow][!] Nhập Tên màu mới của bạn.[/bold yellow]")
                new_name = Prompt.ask("[bold yellow][?] Tên[/bold yellow]")
                console.print("[bold #00dcff][%] Đang lưu dữ liệu[/bold #00dcff]: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 30:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        console.print("[bold green]Đã thành công.[/bold green]")
                        console.print("[bold green]==================================[/bold green]")
                        answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold blue][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold blue][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                        else: continue
                    else:
                        console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                        console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Vui lòng sử dụng giá trị hợp lệ ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[bold yellow][%] Đang tạo một biển số xe [/bold yellow]: ", end=None)
                if cpm.set_player_plates():
                    console.print("[bold green]Đã thành công.[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff]: [bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                    else: continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                console.print("[bold yellow]Ghi chú: ⚠ Sau khi xóa tài khoản của bạn, sẽ không thể quay lại ⚠[/bold yellow]")
                answ = Prompt.ask("[bold yellow][?] Bạn có muốn xóa tài khoản này không?[/bold yellow]", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    console.print("[bold #00dcff][%] Đang xóa tài khoản của bạn[/bold #00dcff]: [bold green]Đã thành công.[/bold green]")
                    console.print("==================================")
                    console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold blue]")
                else: continue
            elif service == 9: # Account Register
                console.print("[bold yellow][!] Đăng ký tài khoản mới.[/bold yellow]")
                acc2_email = prompt_valid_value("[bold yellow][?] Email tài khoản   : [/bold yellow]", "Email", password=False)
                acc2_password = prompt_valid_value("[bold yellow][?] Mật khẩu tài khoản: [/bold yellow]", "Password", password=False)
                console.print("[bold #00dcff][%] Đang tạo tài khoản mới [/bold #00dcff]: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    console.print("[bold green]Đã thành công.[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    console.print(f"[bold yellow]Ghi chú: Để điều chỉnh tài khoản này bằng tool cpk1[/bold yellow]")
                    console.print("[bold yellow]bạn phải đăng nhập vào game bằng tài khoản này.[/bold yellow]")
                    sleep(2)
                    continue
                elif status == 105:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow][!] Email này đã tồn tại.[/bold yellow]")
                    sleep(2)
                    continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[bold yellow][%] Xóa bạn bè của bạn[/bold yellow]: ", end=None)
                if cpm.delete_player_friends():
                    console.print("[bold green]Đã thành công[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                    else: continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 11: # Unlock All Paid Cars
                console.print("[bold yellow]! Ghi chú: chức năng này mất một thời gian để hoàn thành, vui lòng không hủy.[/bold yellow]", end=None)
                console.print("[bold yellow][%] Mở khóa tất cả các xe trả tiền [/bold yellow]: ", end=None)
                if cpm.unlock_paid_cars():
                    console.print("[bold green]Đã thành công.[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold blue][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold blue][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold blue]")
                    else: continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Cars
                console.print("[bold yellow][%] Mở khóa tất cả các xe[/bold yellow]: ", end=None)
                if cpm.unlock_all_cars():
                    console.print("[bold green]Đã thành công.[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold blue]")
                    else: continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 13: # Unlock All Cars Siren
                console.print("[bold yellow][%] Mở khóa tất cả còi báo động[/bold yellow]: ", end=None)
                if cpm.unlock_all_cars_siren():
                    console.print("[bold green]Đã thành công[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold blue]")
                    else: continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 14: # Unlock w16 Engine
                console.print("[bold yellow][%] Mở khóa động cơ w16[/bold yellow]: ", end=None)
                if cpm.unlock_w16():
                    console.print("[bold green]Đã thành công.[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold blue]")
                    else: continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 15: # Unlock All Horns
                console.print("[bold yellow][%] Mở khóa tất cả còi xe[/bold yellow]: ", end=None)
                if cpm.unlock_horns():
                    console.print("[bold green]Đã thành công.[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold blue]")
                    else: continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[bold yellow][%] Mở khóa không hỏng động cơ[/bold yellow]: ", end=None)
                if cpm.disable_engine_damage():
                    console.print("[bold green]Thành công.[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                    else: continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[bold yellow][%] Mở khóa không giới hạn xăng[/bold yellow]: ", end=None)
                if cpm.unlimited_fuel():
                    console.print("[bold green]Đã thành công.[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                    else: continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[bold yellow][%] Mở khóa nhà 3[/bold yellow]: ", end=None)
                if cpm.unlock_houses():
                    console.print("[bold green]Đã thành công.[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                    else: continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[bold yellow][%] Mở khóa khói[/bold yellow]: ", end=None)
                if cpm.unlock_smoke():
                    console.print("[bold green]Đã Thành công.[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                    else: continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 20: # Change Races Wins
                console.print("[bold yellow][!] Chỉnh sửa số cuộc đua bạn thắng.[/bold yellow]")
                amount = IntPrompt.ask("[bold yellow][?] số lượng[/bold yellow]")
                console.print("[bold green][%] Đang thay đổi dữ liệu của bạn[/bold green]: ", end=None)
                if amount > 0 and amount <= 999:
                    if cpm.set_player_wins(amount):
                        console.print("[bold green]Đã thành công.[/bold green]")
                        console.print("[bold green]==================================[/bold green]")
                        answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                        else: continue
                    else:
                        console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                        console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Vui lòng sử dụng giá trị hợp lệ ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 21: # Change Races Loses
                console.print("[bold yellow][!] Chỉnh sửa số cuộc đua bạn thua[/bold yellow]")
                amount = IntPrompt.ask("[bold yellow][?] Số lượng[/bold yellow]")
                console.print("[bold green][%] Đang thay đổi dữ liệu của bạn[/bold green]: ", end=None)
                if amount > 0 and amount <= 999:
                    if cpm.set_player_loses(amount):
                        console.print("[bold green]Đã thành công.[/bold green]")
                        console.print("[bold green]==================================[/bold green]")
                        answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                        else: continue
                    else:
                        console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                        console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Vui lòng sử dụng giá trị hợp lệ ⚠[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 22: # Clone Account
                console.print("[bold yellow][?] Vui lòng nhập chi tiết tài khoản[/bold yellow]:")
                to_email = prompt_valid_value("[bold yellow][?] Email tài khoản   :[/bold yellow]", "Email", password=False)
                to_password = prompt_valid_value("[bold yellow][?] Mật khẩu tài khoản:[/bold yellow]", "Password", password=False)
                console.print("[bold #00dcff][%] Đang sao chép tài khoản của bạn[/bold #00dcff]: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    console.print("[bold green]Đã thành công.[/bold green]")
                    console.print("[bold green]==================================[/bold green]")
                    answ = Prompt.ask("[bold yellow][?] Bạn có muốn thoát không ?[/bold yellow]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold #00dcff][!] Cảm ơn bạn đã sử dụng tool của tôi[/bold #00dcff][bold yellow]《 Telegram: @{__CHANNEL_USERNAME__} 》[/bold yellow]")
                    else: continue
                else:
                    console.print("[bold red]⚠ Thất bại ⚠[/bold red]")
                    console.print("[bold yellow]⚠ Hãy thử lại ⚠[/bold yellow]")
                    sleep(2)
                    continue
            else: continue
            break
        break
