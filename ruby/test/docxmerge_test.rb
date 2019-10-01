require "test_helper"

class DocxmergeTest < Minitest::Test
  def test_render_template
    docxmerge = get_docxmerge
    data = {
        "logo" => "https://docxmerge.com/assets/android-chrome-512x512.png",
        "name" => "James bond",
    }
    docxmerge.render_template("hello_world", data, "PDF")
  end

  def test_render_file
    docxmerge = get_docxmerge
    file_path = "/disco-grande/projects/docxmerge-sdk/ruby/fixtures/hello_world.docx"
    file = File.open(file_path, "rb")
    data = {
        "logo" => "https://docxmerge.com/assets/android-chrome-512x512.png",
        "name" => "James bond",
    }
    docxmerge.render_file(file, data, "PDF")
  end

  def test_render_url
    docxmerge = get_docxmerge
    url = "https://api.docxmerge.com/api/v1/File/GetContenido?id=cdb9842d-5e38-4149-a06b-e1079a208fc3&download=true"
    data = {
        "logo" => "https://docxmerge.com/assets/android-chrome-512x512.png",
        "name" => "James bond",
    }
    docxmerge.render_url(url, data, "PDF")
  end

  private

  def get_docxmerge
    Docxmerge::Docxmerge.new("26JZ5iPpD4U3b9z7lqkXeB2OGsbdF7", "default", "http://localhost:5101")
  end
end
