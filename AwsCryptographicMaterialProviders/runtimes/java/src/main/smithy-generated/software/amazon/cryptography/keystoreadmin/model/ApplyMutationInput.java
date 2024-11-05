// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class ApplyMutationInput {

  private final MutationToken MutationToken;

  /**
   * For Default DynamoDB Table Storage, the maximum page size is 99.
   *   At most, Apply Mutation will mutate pageSize Items.
   *   Note that, at least for Storage:DynamoDBTable,
   *   two additional "item" are consumed by the Mutation Commitment and Mutation Index verification.
   *   Thus, if the pageSize is 24, 26 requests will be sent in the Transact Write Request.
   */
  private final Integer PageSize;

  /**
   * Optional. Defaults to reEncrypt with a default KMS Client.
   */
  private final KeyManagementStrategy Strategy;

  /**
   * Optional. Defaults to TrustStorage. See System Key.
   */
  private final SystemKey SystemKey;

  protected ApplyMutationInput(BuilderImpl builder) {
    this.MutationToken = builder.MutationToken();
    this.PageSize = builder.PageSize();
    this.Strategy = builder.Strategy();
    this.SystemKey = builder.SystemKey();
  }

  public MutationToken MutationToken() {
    return this.MutationToken;
  }

  /**
   * @return For Default DynamoDB Table Storage, the maximum page size is 99.
   *   At most, Apply Mutation will mutate pageSize Items.
   *   Note that, at least for Storage:DynamoDBTable,
   *   two additional "item" are consumed by the Mutation Commitment and Mutation Index verification.
   *   Thus, if the pageSize is 24, 26 requests will be sent in the Transact Write Request.
   */
  public Integer PageSize() {
    return this.PageSize;
  }

  /**
   * @return Optional. Defaults to reEncrypt with a default KMS Client.
   */
  public KeyManagementStrategy Strategy() {
    return this.Strategy;
  }

  /**
   * @return Optional. Defaults to TrustStorage. See System Key.
   */
  public SystemKey SystemKey() {
    return this.SystemKey;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder MutationToken(MutationToken MutationToken);

    MutationToken MutationToken();

    /**
     * @param PageSize For Default DynamoDB Table Storage, the maximum page size is 99.
     *   At most, Apply Mutation will mutate pageSize Items.
     *   Note that, at least for Storage:DynamoDBTable,
     *   two additional "item" are consumed by the Mutation Commitment and Mutation Index verification.
     *   Thus, if the pageSize is 24, 26 requests will be sent in the Transact Write Request.
     */
    Builder PageSize(Integer PageSize);

    /**
     * @return For Default DynamoDB Table Storage, the maximum page size is 99.
     *   At most, Apply Mutation will mutate pageSize Items.
     *   Note that, at least for Storage:DynamoDBTable,
     *   two additional "item" are consumed by the Mutation Commitment and Mutation Index verification.
     *   Thus, if the pageSize is 24, 26 requests will be sent in the Transact Write Request.
     */
    Integer PageSize();

    /**
     * @param Strategy Optional. Defaults to reEncrypt with a default KMS Client.
     */
    Builder Strategy(KeyManagementStrategy Strategy);

    /**
     * @return Optional. Defaults to reEncrypt with a default KMS Client.
     */
    KeyManagementStrategy Strategy();

    /**
     * @param SystemKey Optional. Defaults to TrustStorage. See System Key.
     */
    Builder SystemKey(SystemKey SystemKey);

    /**
     * @return Optional. Defaults to TrustStorage. See System Key.
     */
    SystemKey SystemKey();

    ApplyMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationToken MutationToken;

    protected Integer PageSize;

    protected KeyManagementStrategy Strategy;

    protected SystemKey SystemKey;

    protected BuilderImpl() {}

    protected BuilderImpl(ApplyMutationInput model) {
      this.MutationToken = model.MutationToken();
      this.PageSize = model.PageSize();
      this.Strategy = model.Strategy();
      this.SystemKey = model.SystemKey();
    }

    public Builder MutationToken(MutationToken MutationToken) {
      this.MutationToken = MutationToken;
      return this;
    }

    public MutationToken MutationToken() {
      return this.MutationToken;
    }

    public Builder PageSize(Integer PageSize) {
      this.PageSize = PageSize;
      return this;
    }

    public Integer PageSize() {
      return this.PageSize;
    }

    public Builder Strategy(KeyManagementStrategy Strategy) {
      this.Strategy = Strategy;
      return this;
    }

    public KeyManagementStrategy Strategy() {
      return this.Strategy;
    }

    public Builder SystemKey(SystemKey SystemKey) {
      this.SystemKey = SystemKey;
      return this;
    }

    public SystemKey SystemKey() {
      return this.SystemKey;
    }

    public ApplyMutationInput build() {
      if (Objects.isNull(this.MutationToken())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationToken`"
        );
      }
      return new ApplyMutationInput(this);
    }
  }
}
