require 'json'

class GradeProgress
  def initialize

    file = open("data/grades.json")
    json = file.read

    @grades = JSON.parse(json)

  end


  def print_grades
      @grades
  end

  def thing
    @grades.each do |key, value|

      value.each do |grade|
        puts grade

      end

    end

  end
end



new_grade = GradeProgress.new

puts new_grade.thing
