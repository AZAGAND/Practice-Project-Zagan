import time

def tampilkan_lirik(delay_huruf, delay_baris):
    lirik = [
        "dulu sakit, sekarang lega",
        "cerita lama, aku dah reda",
        "tak nak pusing, tak nak tanya",
        "aku kuat, tanpa drama",
        "dulu sakit, sekarang lega",
        "cerita lama, aku dah reda",
        "tak nak pusing, tak nak tanya",
        "aku kuat, tanpa drama",
        "aku dah lupa, tak ingat lagi",
        "nama kau pun hilang dari hati",
        "aku move on, hidup sendiri",
        "tak perlu kau, aku heppy",
        "aku dah lupa, tak ingat lagi",
        "nama kau pun hilang dari hati",
        "aku move on, hidup sendiri",
        "tak perlu kau, aku heppy",
    ]
    

    for i, baris in enumerate (lirik):
        for huruf in baris:
            print(huruf, end="", flush=True)
            time.sleep(delay_baris[i])

        print()
        time.sleep(delay_huruf[i])    

delay_huruf = [0.08, 0.08, 0.09, 0.10, 0.08, 0.09, 0.07, 0.12, 0.07, 0.07, 0.08, 0.08, 0.09, 0.08, 0.09, 0.08]      
delay_baris = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.31, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

print("\n" * 10)

tampilkan_lirik( delay_baris, delay_huruf)
