import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const LearnyApp());
}

class LearnyApp extends StatelessWidget {
  const LearnyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Learny',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const HomeScreen(),
    );
  }
}
