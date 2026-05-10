import 'package:flutter/material.dart';
import '../widgets/learning_card.dart';
import '../models/learning_content.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  final List<LearningContent> contents = const [
    LearningContent(
      title: '수학 기초',
      description: '기초 수학 개념을 배워요.',
      difficulty: 1,
    ),
    LearningContent(
      title: '과학 탐험',
      description: '과학 실험을 직접 해보아요.',
      difficulty: 2,
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Learny 홈')), 
      body: ListView.builder(
        itemCount: contents.length,
        itemBuilder: (context, index) {
          return LearningCard(content: contents[index]);
        },
      ),
    );
  }
}
