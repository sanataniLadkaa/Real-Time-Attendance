insert into public.training_jobs (job_name, dataset_path, status, started_at)
values ('autotrain-schedule', 'supabase://bucket/raw_videos/', 'pending', now());
