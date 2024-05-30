module "vnet" {
  source      = "./modules/vnet"
  vnet_cidr   = "10.0.0.0/16"
  subnet_cidr = "10.0.1.0/24"
}

module "vm" {
  source            = "./modules/vm"
  vm_name           = "example-vm"
  vm_size           = "Standard_B1s"
  admin_username    = "adminuser"
  admin_password    = "P@ssw0rd1234!"  # Replace with a secure password
  subnet_id         = module.vnet.subnet_id
  vnet_resource_group = module.vnet.resource_group_name
}

output "vnet_id" {
  value = module.vnet.vnet_id
}

output "vm_id" {
  value = module.vm.vm_id
}
