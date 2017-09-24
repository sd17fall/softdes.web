require 'shellwords'
require 'rake/clean'

task default: %w[notebooks handouts]

SOURCE_MAP = {}

rule ".pdf" => ->(f){SOURCE_MAP[f]} do |t|
  mkdir_p File.dirname(t.name), :verbose => false
  sh "pandoc #{t.source} -o #{t.name} -s --highlight-style pygments -V geometry:margin=1in"
end

rule ".html" => ->(f){SOURCE_MAP[f]} do |t|
  mkdir_p File.dirname(t.name), :verbose => false
  sh "pandoc #{t.source} -o #{t.name} -s --highlight-style pygments --mathjax"
end

for md in Dir["files/activities/**/*.md"] do
  out = md.sub('/activities/', '/handouts/')
  pdf = out.sub(/\.md$/, '.pdf')
  html = out.sub(/\.md$/, '.html')
  SOURCE_MAP[html] = md
  SOURCE_MAP[pdf] = md
  multitask :handouts => [pdf, html]
  CLOBBER << pdf << html
end

for src in Dir["notebooks/**/*.ipynb"] do
  target = src.sub(%r'^notebooks/', 'notes/').sub('.ipynb', '.md')
  task :notebooks => target
  CLOBBER << target
  file target => src do |t|
    sh "jupyter nbconvert #{Shellwords.escape t.sources[0]} --to markdown --output-dir #{Shellwords.escape File.dirname t.name} --template=config/nb_md.tpl"
  end
end
