from flask import Flask, request, jsonify

from cipher.caesar import CaesarCipher 

app = Flask(__name__)

# Khởi tạo đối tượng từ Class đã import đúng
cipher_tool = CaesarCipher() 

@app.route('/api/caesar/encrypt', methods=['POST'])
def api_encrypt():  # Đổi tên hàm để phân biệt với cipher_tool.encrypt_text
    data = request.get_json() or {}
    text = data.get('text', '')
    
    try:
        shift = int(data.get('shift', 0))  # Ép kiểu số nguyên để tránh lỗi tính toán
    except (ValueError, TypeError):
        return jsonify({'error': 'Tham số shift phải là số nguyên!'}), 400
    
    encrypted_text = cipher_tool.encrypt_text(text, shift) 
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def api_decrypt():  # Đổi tên hàm
    data = request.get_json() or {}
    text = data.get('text', '')
    
    try:
        shift = int(data.get('shift', 0))
    except (ValueError, TypeError):
        return jsonify({'error': 'Tham số shift phải là số nguyên!'}), 400
        
    decrypted_text = cipher_tool.decrypt_text(text, shift)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)