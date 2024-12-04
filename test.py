import requests

# Define the input text and max_new_tokens
input_text = "hello"
max_new_tokens = 10

# Set the constant target language (e.g., "arb_Arab")
target_lang = "arb_Arab"

# List of language codes (source languages)
languages = [
    "ace_Arab", "ace_Latn", "acm_Arab", "acq_Arab", "aeb_Arab", "afr_Latn", "ajp_Arab", "aka_Latn",
    "amh_Ethi", "apc_Arab", "arb_Arab", "arb_Latn", "ars_Arab", "ary_Arab", "arz_Arab", "asm_Beng",
    "ast_Latn", "awa_Deva", "ayr_Latn", "azb_Arab", "azj_Latn", "bak_Cyrl", "bam_Latn", "ban_Latn",
    "bel_Cyrl", "bem_Latn", "ben_Beng", "bho_Deva", "bjn_Arab", "bjn_Latn", "bod_Tibt", "bos_Latn",
    "bug_Latn", "bul_Cyrl", "cat_Latn", "ceb_Latn", "ces_Latn", "cjk_Latn", "ckb_Arab", "crh_Latn",
    "cym_Latn", "dan_Latn", "deu_Latn", "dik_Latn", "dyu_Latn", "dzo_Tibt", "ell_Grek", "eng_Latn",
    "epo_Latn", "est_Latn", "eus_Latn", "ewe_Latn", "fao_Latn", "fij_Latn", "fin_Latn", "fon_Latn",
    "fra_Latn", "fur_Latn", "fuv_Latn", "gla_Latn", "gle_Latn", "glg_Latn", "grn_Latn", "guj_Gujr",
    "hat_Latn", "hau_Latn", "heb_Hebr", "hin_Deva", "hne_Deva", "hrv_Latn", "hun_Latn", "hye_Armn",
    "ibo_Latn", "ilo_Latn", "ind_Latn", "isl_Latn", "ita_Latn", "jav_Latn", "jpn_Jpan", "kab_Latn",
    "kac_Latn", "kam_Latn", "kan_Knda", "kas_Arab", "kas_Deva", "kat_Geor", "knc_Arab", "knc_Latn",
    "kaz_Cyrl", "kbp_Latn", "kea_Latn", "khm_Khmr", "kik_Latn", "kin_Latn", "kir_Cyrl", "kmb_Latn",
    "kmr_Latn", "kon_Latn", "kor_Hang", "lao_Laoo"
]

# API endpoint
url = 'http://localhost:8000/translate'

# Loop through each language code and make the request
for lang in languages:
    # Use the current language as the source language
    source_lang = lang
    
    # Prepare the payload for the request
    payload = {
        "input_text": input_text,
        "source_lang": source_lang,
        "target_lang": target_lang,
        "max_new_tokens": max_new_tokens
    }

    # Send the POST request
    response = requests.post(url, json=payload, headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    })

    # Check if the request was successful
    if response.status_code == 200:
        print(f"Translation successful for {source_lang}")
    else:
        print(f"Error for {source_lang}: {response.status_code}")
