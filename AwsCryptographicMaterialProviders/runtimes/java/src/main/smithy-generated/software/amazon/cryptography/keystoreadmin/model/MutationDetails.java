// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class MutationDetails {

  /**
   * The original properities of the Branch Key.
   */
  private final MutableBranchKeyProperities Original;

  /**
   * The terminal properities of the Branch Key.
   */
  private final MutableBranchKeyProperities Terminal;

  /**
   * The input for this mutation.
   */
  private final Mutations Input;

  /**
   * String descprition of the System Key.
   */
  private final String SystemKey;

  /**
   * ISO 8601 time when the mutation was initialized.
   */
  private final String CreateTime;

  /**
   * UUID of the Mutation.
   */
  private final String UUID;

  protected MutationDetails(BuilderImpl builder) {
    this.Original = builder.Original();
    this.Terminal = builder.Terminal();
    this.Input = builder.Input();
    this.SystemKey = builder.SystemKey();
    this.CreateTime = builder.CreateTime();
    this.UUID = builder.UUID();
  }

  /**
   * @return The original properities of the Branch Key.
   */
  public MutableBranchKeyProperities Original() {
    return this.Original;
  }

  /**
   * @return The terminal properities of the Branch Key.
   */
  public MutableBranchKeyProperities Terminal() {
    return this.Terminal;
  }

  /**
   * @return The input for this mutation.
   */
  public Mutations Input() {
    return this.Input;
  }

  /**
   * @return String descprition of the System Key.
   */
  public String SystemKey() {
    return this.SystemKey;
  }

  /**
   * @return ISO 8601 time when the mutation was initialized.
   */
  public String CreateTime() {
    return this.CreateTime;
  }

  /**
   * @return UUID of the Mutation.
   */
  public String UUID() {
    return this.UUID;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Original The original properities of the Branch Key.
     */
    Builder Original(MutableBranchKeyProperities Original);

    /**
     * @return The original properities of the Branch Key.
     */
    MutableBranchKeyProperities Original();

    /**
     * @param Terminal The terminal properities of the Branch Key.
     */
    Builder Terminal(MutableBranchKeyProperities Terminal);

    /**
     * @return The terminal properities of the Branch Key.
     */
    MutableBranchKeyProperities Terminal();

    /**
     * @param Input The input for this mutation.
     */
    Builder Input(Mutations Input);

    /**
     * @return The input for this mutation.
     */
    Mutations Input();

    /**
     * @param SystemKey String descprition of the System Key.
     */
    Builder SystemKey(String SystemKey);

    /**
     * @return String descprition of the System Key.
     */
    String SystemKey();

    /**
     * @param CreateTime ISO 8601 time when the mutation was initialized.
     */
    Builder CreateTime(String CreateTime);

    /**
     * @return ISO 8601 time when the mutation was initialized.
     */
    String CreateTime();

    /**
     * @param UUID UUID of the Mutation.
     */
    Builder UUID(String UUID);

    /**
     * @return UUID of the Mutation.
     */
    String UUID();

    MutationDetails build();
  }

  static class BuilderImpl implements Builder {

    protected MutableBranchKeyProperities Original;

    protected MutableBranchKeyProperities Terminal;

    protected Mutations Input;

    protected String SystemKey;

    protected String CreateTime;

    protected String UUID;

    protected BuilderImpl() {}

    protected BuilderImpl(MutationDetails model) {
      this.Original = model.Original();
      this.Terminal = model.Terminal();
      this.Input = model.Input();
      this.SystemKey = model.SystemKey();
      this.CreateTime = model.CreateTime();
      this.UUID = model.UUID();
    }

    public Builder Original(MutableBranchKeyProperities Original) {
      this.Original = Original;
      return this;
    }

    public MutableBranchKeyProperities Original() {
      return this.Original;
    }

    public Builder Terminal(MutableBranchKeyProperities Terminal) {
      this.Terminal = Terminal;
      return this;
    }

    public MutableBranchKeyProperities Terminal() {
      return this.Terminal;
    }

    public Builder Input(Mutations Input) {
      this.Input = Input;
      return this;
    }

    public Mutations Input() {
      return this.Input;
    }

    public Builder SystemKey(String SystemKey) {
      this.SystemKey = SystemKey;
      return this;
    }

    public String SystemKey() {
      return this.SystemKey;
    }

    public Builder CreateTime(String CreateTime) {
      this.CreateTime = CreateTime;
      return this;
    }

    public String CreateTime() {
      return this.CreateTime;
    }

    public Builder UUID(String UUID) {
      this.UUID = UUID;
      return this;
    }

    public String UUID() {
      return this.UUID;
    }

    public MutationDetails build() {
      if (Objects.isNull(this.Original())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Original`"
        );
      }
      if (Objects.isNull(this.Terminal())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Terminal`"
        );
      }
      if (Objects.isNull(this.Input())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Input`"
        );
      }
      if (Objects.isNull(this.SystemKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `SystemKey`"
        );
      }
      if (Objects.isNull(this.CreateTime())) {
        throw new IllegalArgumentException(
          "Missing value for required field `CreateTime`"
        );
      }
      if (Objects.isNull(this.UUID())) {
        throw new IllegalArgumentException(
          "Missing value for required field `UUID`"
        );
      }
      return new MutationDetails(this);
    }
  }
}
