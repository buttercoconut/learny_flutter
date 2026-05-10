import 'package:http/http.dart' as http;

class AuthService {
  final String baseUrl;
  AuthService({required this.baseUrl});

  Future<bool> login(String username, String password) async {
    final response = await http.post(
      Uri.parse('$baseUrl/login'),
      body: {'username': username, 'password': password},
    );
    return response.statusCode == 200;
  }
}
