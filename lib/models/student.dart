class Student {
  final String name;
  final int grade;
  final int level;

  Student({required this.name, required this.grade, required this.level});

  Map<String, dynamic> toJson() => {
        'name': name,
        'grade': grade,
        'level': level,
      };
}
