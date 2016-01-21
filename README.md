# YAML-based Puppet ENC

This is a simple Puppet ENC (External Node Classifier) that classifies
nodes based on regular expressions read from a YAML file.

## Configuration File Format

The configuration file is a YAML dictionary where each key represents a host
regular expression. If no match is found, attributes from the (optional) host
_DEFAULT_ is returned.

The following attributes are allowed by Puppet:

- environment
- classes
- parameters

At least _environment_ or _classes_ must be defined.


## Configuration Example

    DEFAULT:
      classes: []
    
    '^foo-dev-bar\d+\..+$':
      environment: develop
      parameters:  { guild: foo-dev }
      classes: [ 'roles::foo::bar' ]
    
    '^foo-prod-bar\d+\..+$':
      environment: production
      parameters:  { guild: foo-prod }
      classes: [ 'roles::foo::bar' ]
