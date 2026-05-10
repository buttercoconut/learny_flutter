class LearningContent {
  final String title;
  final String description;
  final int difficulty;

  const LearningContent({required this.title, required this.description, required this.difficulty});

  Map<String, dynamic> toJson() => {
        'title': title,
        'description': description,
        'difficulty': difficulty,
      };
}
