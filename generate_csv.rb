require 'fileutils'

train_data_path = "./data/train/data.txt"
test_data_path = "./data/test/data.txt"

FileUtils.touch(train_data_path) unless FileTest.exist?(train_data_path)
FileUtils.touch(test_data_path) unless FileTest.exist?(test_data_path)


test_clinton_data_paths = Dir.glob("./data/test/clinton/*.jpg")
test_may_data_paths = Dir.glob("./data/test/may/*.jpg")
test_merkel_data_paths = Dir.glob("./data/test/merkel/*.jpg")
train_clinton_data_paths = Dir.glob("./data/train/clinton/*.jpg")
train_may_data_paths = Dir.glob("./data/train/may/*.jpg")
train_merkel_data_paths = Dir.glob("./data/train/merkel/*.jpg")


File.open(test_data_path, "w") do |f|
  test_clinton_data_paths.each { |path| f.puts("#{path} 0") }
  test_may_data_paths.each { |path| f.puts("#{path} 1") }
  test_merkel_data_paths.each { |path| f.puts("#{path} 2") }
end
File.open(train_data_path, "w") do |f|
  train_clinton_data_paths.each { |path| f.puts("#{path} 0") }
  train_may_data_paths.each { |path| f.puts("#{path} 1") }
  train_merkel_data_paths.each { |path| f.puts("#{path} 2") }
end