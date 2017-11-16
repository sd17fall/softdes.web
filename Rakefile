require 'shellwords'
require 'time'
require 'rake/clean'

task default: %w[notebooks handouts]

SOURCE_MAP = {}
NOTEBOOK_TEMPLATE = "config/nb_md.tpl"

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
  target = src.sub(%r'^notebooks/', '_notebooks/').sub('.ipynb', '.md')
  multitask :notebooks => target
  CLOBBER << target
  file target => [src, NOTEBOOK_TEMPLATE] do |t|
    # use git of file.mtime to find date
    # convert to stdout and capture this
    # add a date:
    # sh "jupyter nbconvert #{Shellwords.escape source} --to markdown --output-dir #{Shellwords.escape File.dirname t.name} --template=#{Shellwords.escape TPL}"
    source = t.sources[0]
    file_mtime = `git log --diff-filter=A --follow --format=%aI --date=iso -- #{Shellwords.escape source} | tail -1`.chomp
    if file_mtime.empty?
      file_mtime = File.mtime(source).iso8601
    end
    content =`jupyter nbconvert #{Shellwords.escape source} --to markdown --template=#{Shellwords.escape NOTEBOOK_TEMPLATE} --stdout`
    content = content.sub('%MODTIME%', file_mtime)
    content = content.sub('%SOURCE%', source)
    open(t.name, 'w') do |fd|
      fd.write content
    end
  end
end
