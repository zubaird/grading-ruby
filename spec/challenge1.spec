require 'json'

class GradeProgress

  def initialize(data)

    @grades = data

  end


  def print_grades
    @grades
  end

  def difference
    @grades.each do |key, value|

      value.each do |grade|
        puts grade

      end

    end

  end
end



describe GradeProgress do

  GRADES = {
    :"Bryon Zieme" => [18, 57, 91, 63, 17, 36, 87, 40, 38, 40, 43, 57],
  }

  SORTED = {
    :"Bryon Zieme" => [:up, :up, :down,:down, :up, :up, :down, :down, :up, :up, :up, :up],
  }

  describe "#print_grades" do
    it "It returns GRADES" do
      grade_progress = GradeProgress.new(GRADES)

      results = grade_progress.print_grades

      expect(results).to eq(GRADES)
    end
  end

  describe "#difference" do
    it "returns the differences" do
      grade_progress = GradeProgress.new(GRADES)

      difference = grade_progress.difference

      expect(difference).to eq(SORTED)
    end
  end

end
