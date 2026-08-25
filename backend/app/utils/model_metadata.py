from app.models.model_metadata import ModelMetadata


def build_model_response(
    trained_model,
    metrics,
    model_path
):
    return ModelMetadata(
        model_id=trained_model.id,
        model_name=getattr(
            trained_model,
            "name",
            trained_model.id
        ),
        algorithm=trained_model.algorithm,
        problem_type=trained_model.problem_type,
        version=getattr(
            trained_model,
            "version",
            "v1"
        ),
        framework=getattr(
            trained_model,
            "framework",
            "unknown"
        ),
        parameters=getattr(
            trained_model,
            "parameters",
            {}
        ),
        training_info=getattr(
            trained_model,
            "training_info",
            {}
        ),
        metrics=metrics,
        model_path=model_path,
        created_at=trained_model.created_at
    )