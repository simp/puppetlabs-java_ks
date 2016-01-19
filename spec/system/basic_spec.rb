require 'spec_helper_system'

describe 'prep nodes' do
  it 'requires java' do
    puppet_apply(%{
      class { 'java': }
    }) { |r| [0,2].is_expected.to include r.exit_code}
  end
end
