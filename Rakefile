require 'rake/clean'

task default: %w[handouts]

# handouts = []

SOURCE_MAP = {}

rule ".pdf" => ->(f){SOURCE_MAP[f]} do |t|
  mkdir_p File.dirname(t.name), :verbose => false
  sh "pandoc #{t.source} -o #{t.name} -s -t latex --highlight-style pygments -V geometry:margin=1in"
end

rule ".html" => ->(f){SOURCE_MAP[f]} do |t|
  mkdir_p File.dirname(t.name), :verbose => false
  sh "pandoc #{t.source} -o #{t.name} -s -t html --highlight-style pygments --mathjax"
end

for md in Dir["files/activities/**/*.md"] do
  out = md.sub('/activities/', '/handouts/')
  pdf = out.sub(/\.md$/, '.pdf')
  html = out.sub(/\.md$/, '.html')
  SOURCE_MAP[html] = md
  SOURCE_MAP[pdf] = md
  task :handouts => [pdf, html]
  CLOBBER << pdf << html
  # HTML_SOURCES[html] = md
  # file pdf => md do |t|
  #   mkdir_p File.dirname(out), :verbose => false
  #   sh "echo pandoc #{t.prerequisites.first} -o #{t.source} -s -t html --mathjax"
  # end
  # file html => md do |t|
  #   mkdir_p File.dirname(out), :verbose => false
  #   sh "echo pandoc #{t.prerequisites.first} -o #{t.source} -s -t html --mathjax"
  # end
end

# CLOBBER += handouts

# task :handouts => handouts
