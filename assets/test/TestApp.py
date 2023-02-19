import run_app, os

def test_crypt():
    run_app.data.thextention = ".crypt"
    run_app.data.input_value1 = "crypt_decrypt_files/instructions.txt"
    run_app.data.input_value2 = "crypt_decrypt_files/instructions"
    run_app.data.input_value3 = "test"
    run_app.entryFile4()
