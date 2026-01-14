provider "aws" {
  region = "us-east-1"
}

# EKS Cluster for Scalable Microservices
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = "creator-os-cluster"
  cluster_version = "1.27"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  eks_managed_node_groups = {
    general = {
      instance_types = ["t3.medium"]
      min_size     = 2
      max_size     = 5
    }
    # GPU Node Group for Video Rendering & AI Inference
    ai_workers = {
      instance_types = ["g4dn.xlarge"]
      min_size     = 1
      max_size     = 10
      labels = {
        workload = "ai-inference"
      }
      taints = [{
        key    = "dedicated"
        value  = "gpu"
        effect = "NO_SCHEDULE"
      }]
    }
  }
}

# S3 Bucket for Hero Content and Adapted Assets
resource "aws_s3_bucket" "content_store" {
  bucket = "creator-os-assets-prod"
}

resource "aws_s3_bucket_lifecycle_configuration" "content_lifecycle" {
  bucket = aws_s3_bucket.content_store.id
  rule {
    id     = "archive_old_hero_content"
    status = "Enabled"
    transition {
      days          = 30
      storage_class = "GLACIER"
    }
  }
}