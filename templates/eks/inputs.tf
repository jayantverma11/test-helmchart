module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.15.4"
  # other configuration
}

module "cluster_autoscaler_irsa_role" {
  source  = "terraform-aws-modules/iam/aws//modules/iam-role-for-service-accounts-eks"
  version = "v5.42.0"
}
