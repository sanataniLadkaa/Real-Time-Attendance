-- Supabase Schema: Postgres tables for Attendance System

-- employees: basic employee profile
create table if not exists public.employees (
  id uuid primary key default gen_random_uuid(),
  employee_id text not null unique,
  full_name text not null,
  email text,
  phone text,
  department text,
  created_at timestamptz default now()
);

-- face_embeddings: store face embedding meta
create table if not exists public.face_embeddings (
  id uuid primary key default gen_random_uuid(),
  employee_id text references public.employees(employee_id) on delete set null,
  embedding float8[] not null,
  model_version text not null,
  created_at timestamptz default now(),
  source text -- e.g., 'edge_upload' or 'web_upload'
);

-- voice_embeddings: store voice embedding meta
create table if not exists public.voice_embeddings (
  id uuid primary key default gen_random_uuid(),
  employee_id text references public.employees(employee_id) on delete set null,
  embedding float8[] not null,
  model_version text not null,
  created_at timestamptz default now(),
  source text
);

-- attendance_logs
create table if not exists public.attendance_logs (
  id uuid primary key default gen_random_uuid(),
  employee_id text references public.employees(employee_id) on delete set null,
  timestamp timestamptz default now(),
  method text, -- 'face', 'voice', '2fa'
  face_score float8,
  voice_score float8,
  meta jsonb
);

-- model_registry: track models stored in Supabase Storage
create table if not exists public.model_registry (
  id uuid primary key default gen_random_uuid(),
  model_name text,
  model_type text, -- 'face', 'voice', 'detector'
  storage_path text, -- supabase storage path
  version text,
  stage text default 'staging', -- 'staging', 'production', 'archived'
  metrics jsonb,
  created_at timestamptz default now()
);

-- training_jobs: log scheduled or triggered training runs
create table if not exists public.training_jobs (
  id uuid primary key default gen_random_uuid(),
  job_name text,
  dataset_path text,
  status text default 'pending', -- 'pending','running','success','failed'
  logs text,
  started_at timestamptz,
  finished_at timestamptz
);

-- index for embeddings (optional: pgvector if available)
-- If you enable pgvector extension, you can create embedding::vector(512) etc. Example:
-- create extension if not exists vector;
-- alter table public.face_embeddings alter column embedding type vector(512) using embedding::vector;

