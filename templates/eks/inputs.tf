module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "v20.20.0"
  # other configuration
}

module "cluster_autoscaler_irsa_role" {
  source  = "terraform-aws-modules/iam/aws//modules/iam-role-for-service-accounts-eks"
  version = "v5.42.0"
}
