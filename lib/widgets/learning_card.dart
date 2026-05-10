import 'package:flutter/material.dart';
import '../models/learning_content.dart';

class LearningCard extends StatelessWidget {
  final LearningContent content;
  const LearningCard({Key? key, required this.content}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.all(8.0),
      child: ListTile(
        title: Text(content.title),
        subtitle: Text(content.description),
        trailing: Text('난이도 ${content.difficulty}'),
      ),
    );
  }
}
