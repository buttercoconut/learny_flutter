import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl;
  ApiService({required this.baseUrl});

  Future<List> fetchLearningContents() async {
    final response = await http.get(Uri.parse('$baseUrl/learning-contents'));
    if (response.statusCode == 200) {
      final List data = jsonDecode(response.body);
      return data;
    } else {
      throw Exception('Failed to load contents');
    }
  }
}
