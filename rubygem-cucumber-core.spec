#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-cucumber-core
Version  : 2.0.0
Release  : 11
URL      : https://rubygems.org/downloads/cucumber-core-2.0.0.gem
Source0  : https://rubygems.org/downloads/cucumber-core-2.0.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-gherkin
BuildRequires : rubygem-kramdown
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-unindent
BuildRequires : rubygem-yard

%description
#cucumber-core
[![Chat with us](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/cucumber/cucumber-ruby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://secure.travis-ci.org/cucumber/cucumber-ruby-core.svg)](http://travis-ci.org/cucumber/cucumber-ruby-core)
[![Code Climate](https://codeclimate.com/github/cucumber/cucumber-ruby-core.svg)](https://codeclimate.com/github/cucumber/cucumber-ruby-core)
[![Coverage Status](https://coveralls.io/repos/cucumber/cucumber-ruby-core/badge.svg?branch=master)](https://coveralls.io/r/cucumber/cucumber-ruby-core?branch=master)
[![Dependency Status](https://gemnasium.com/cucumber/cucumber-ruby-core.svg)](https://gemnasium.com/cucumber/cucumber-ruby-core)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n cucumber-core-2.0.0
gem spec %{SOURCE0} -l --ruby > rubygem-cucumber-core.gemspec

%build
export LANG=C
gem build rubygem-cucumber-core.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
cucumber-core-2.0.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/cucumber-core-2.0.0
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/cucumber-core-2.0.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/.coveralls.yml
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/.github/ISSUE_TEMPLATE.md
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/.github/PULL_REQUEST_TEMPLATE.md
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/.ruby-gemset
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/HISTORY.md
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/cucumber-core.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/background.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/comment.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/data_table.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/describes_itself.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/doc_string.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/empty_background.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/empty_multiline_argument.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/examples_table.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/feature.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/location.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/names.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/outline_step.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/scenario.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/scenario_outline.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/step.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/ast/tag.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/compiler.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/event.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/event_bus.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/events.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/gherkin/ast_builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/gherkin/document.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/gherkin/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/gherkin/tag_expression.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/gherkin/writer.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/gherkin/writer/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/platform.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/report/summary.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/test/action.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/test/around_hook.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/test/case.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/test/filters.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/test/filters/activate_steps_for_self_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/test/filters/locations_filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/test/filters/name_filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/test/filters/tag_filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/test/result.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/test/runner.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/test/step.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/test/timer.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/lib/cucumber/core/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/capture_warnings.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/coverage.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/ast/background_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/ast/data_table_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/ast/doc_string_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/ast/empty_multiline_argument_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/ast/examples_table_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/ast/location_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/ast/outline_step_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/ast/step_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/compiler_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/event_bus_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/event_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/filter_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/gherkin/parser_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/gherkin/writer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/report/summary_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/test/action_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/test/case_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/test/duration_matcher.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/test/filters/locations_filter_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/test/result_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/test/runner_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/test/step_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core/test/timer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/cucumber/core_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/readme_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cucumber-core-2.0.0/spec/report_api_spy.rb
/usr/lib64/ruby/gems/2.3.0/specifications/cucumber-core-2.0.0.gemspec
