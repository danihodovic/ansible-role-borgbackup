# ansible-role-borgbackup [![Build Status](https://ci.depode.com/api/badges/danihodovic/ansible-role-borgbackup/status.svg)](https://ci.depode.com/danihodovic/ansible-role-borgbackup)

An Ansible role to install [Borg](https://github.com/borgbackup/borg) and [Borgmatic](https://github.com/witten/borgmatic).

Usage
```yaml
- name: Install borg backups
  hosts: db
  tasks:
    - name: Install backups
      tags: borg
      import_role:
        name: ansible-role-borgbackup
      vars:
        borg_password: '{{ vault_borgmatic_password }}'
        borg_ssh_key: '{{ vault_borgmatic_ssh_key }}'
        borgmatic_config:
          location:
            repositories:
              - repo@repo.borgbase.com:repo
          hooks:
            postgresql_databases:
              - name: all
                hostname: localhost
                username: '{{ postgres_user }}'
                password: '{{ vault_postgres_password }}'
                ssl_mode: disable
```
