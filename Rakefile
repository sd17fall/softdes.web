require 'rake/clean'

task default: %w[handouts]

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
  html = src.sub(%r'^notebooks/', 'files/notes/').sub('.ipynb', '.html')
  task :notebooks => html
  CLOBBER << html
  file html => src do |t|
    sh "jupyter nbconvert --to html --output-dir #{File.dirname(html)} #{src}"
  end
end
